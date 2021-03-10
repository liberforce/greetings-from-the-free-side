import logging
import os.path
import subprocess

from blog2pelican.repositories.wordpress import decode_wp_content

logger = logging.getLogger(__name__)


class PandocAdapter:
    def __init__(self, *args, **kwargs):
        self._version = None
        self.name = "Pandoc"

    def _get_version(self):
        version = ()

        cmd = ["pandoc", "--version"]
        try:
            output = subprocess.run(cmd, check=True)
            version = tuple(int(i) for i in output.split()[1].split("."))
        except FileNotFoundError:
            logger.warning(
                "Pandoc not found, please check it is installed and in your PATH."
            )
        except (subprocess.CalledProcessError, OSError, ValueError) as e:
            logger.warning("Pandoc version unknown: %s", e)

        return version

    @property
    def version(self):
        if self._version is None:
            self._version = self._get_version()

        return self._version

    @property
    def available(self):
        return bool(self.version)

    def supports(self, input_format):
        return input_format in ("html", "wp-html")

    def adapt(
        self,
        in_markup,
        out_markup,
        output_path,
        filename,
        content,
        strip_raw,
        wp_attach,
        links,
        out_filename,
    ):
        if not self.supports(in_markup):
            return content

        html_filename = os.path.join(output_path, filename + ".html")

        with open(html_filename, "w", encoding="utf-8") as fp:
            # Replace newlines with paragraphs wrapped with <p> so
            # HTML is valid before conversion
            if in_markup == "wp-html":
                new_content = decode_wp_content(content)
            else:
                paragraphs = content.splitlines()
                paragraphs = ["<p>{0}</p>".format(p) for p in paragraphs]
                new_content = "".join(paragraphs)

            fp.write(new_content)

        if self.version < (2,):
            parse_raw = "--parse-raw" if not strip_raw else ""
            wrap_none = (
                "--wrap=none" if self.version >= (1, 16) else "--no-wrap"
            )
            cmd = (
                "pandoc --normalize {0} --from=html"
                ' --to={1} {2} -o "{3}" "{4}"'
            )
            cmd = cmd.format(
                parse_raw,
                out_markup,
                wrap_none,
                out_filename,
                html_filename,
            )
        else:
            from_arg = "-f html+raw_html" if not strip_raw else "-f html"
            cmd = 'pandoc {0} --to={1}-smart --wrap=none -o "{2}" "{3}"'
            cmd = cmd.format(from_arg, out_markup, out_filename, html_filename)

        try:
            rc = subprocess.call(cmd, shell=True)
            if rc < 0:
                error = "Child was terminated by signal %d" % -rc
                exit(error)

            elif rc > 0:
                error = "Please, check your Pandoc installation."
                exit(error)
        except OSError as e:
            error = "Pandoc execution failed: %s" % e
            exit(error)

        os.remove(html_filename)

        with open(out_filename, "r", encoding="utf-8") as fs:
            content = fs.read()
            if out_markup == "markdown":
                # In markdown, to insert a <br />, end a line with two
                # or more spaces & then a end-of-line
                content = content.replace("\\\n ", "  \n")
                content = content.replace("\\\n", "  \n")

        if wp_attach and links:
            content = self.update_links_to_attached_files(content, links)

        return content

    def update_links_to_attached_files(content, attachments):
        for old_url, new_path in attachments.items():
            # url may occur both with http:// and https://
            http_url = old_url.replace("https://", "http://")
            https_url = old_url.replace("http://", "https://")
            for url in [http_url, https_url]:
                content = content.replace(url, "{static}" + new_path)
        return content
