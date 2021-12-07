from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'mdjguyane'  # <storage_account_name>
    account_key = '7hmMiMYJRU6mqzwWsmzW/v9OA2/7peBTB4gAfS9U+hg0C0isDgGgIwcwJ1oeE2zf06h2csDjwsgKK5Lir+ha7Q=='  # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'mdjguyane'  # <storage_account_name>
    account_key = '7hmMiMYJRU6mqzwWsmzW/v9OA2/7peBTB4gAfS9U+hg0C0isDgGgIwcwJ1oeE2zf06h2csDjwsgKK5Lir+ha7Q=='  # <storage_account_key>
    azure_container = 'static'
    expiration_secs = None


class AzureStaticfilesStorage(AzureStorage):
    account_name = 'mdjguyane'  # <storage_account_name>
    account_key = '7hmMiMYJRU6mqzwWsmzW/v9OA2/7peBTB4gAfS9U+hg0C0isDgGgIwcwJ1oeE2zf06h2csDjwsgKK5Lir+ha7Q=='  # <storage_account_key>
    azure_container = 'staticfiles'
    expiration_secs = None
