from blog2pelican.services.migration import Blog2PelicanMigrationService
from blog2pelican.repositories.dotclear import DotclearRepository


def test_dotclear_migration_service():
    service = Blog2PelicanMigrationService()
    output_dir = "content"
    repository = DotclearRepository(
        "tests/data/repositories/dotclear/simple.txt",
    )
    output_markup = "markdown"
    service.migrate_blog_to_pelican(
        repository,
        output_dir,
        output_markup,
    )
