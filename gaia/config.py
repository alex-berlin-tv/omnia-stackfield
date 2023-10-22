import typed_settings as ts


@ts.settings
class Settings:
    port: int
    stackfield_task_uuid: str


settings = ts.load(Settings, appname="gaia", config_files=["settings.toml"])