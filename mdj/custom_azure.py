from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'mdjguyane' # <storage_account_name>
    account_key = '9+VrgsVyEvnbXjxbrC768H5qd6LwmvqQ/55RiLN1xlna9UlorACLwFkrQuu2p/6MmKbkBiTKnugt1XLT56wV7w==' # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'mdjguyane' # <storage_account_name>
    account_key = '9+VrgsVyEvnbXjxbrC768H5qd6LwmvqQ/55RiLN1xlna9UlorACLwFkrQuu2p/6MmKbkBiTKnugt1XLT56wV7w==' # <storage_account_key>
    azure_container = 'static'
    expiration_secs = None