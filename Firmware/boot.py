from kmk.bootcfg import bootcfg

bootcfg(
    autoreload: bool = True,
    boot_device: int = 0,
    cdc_console: bool = True,
    cdc_data: bool = False,
    consumer_control: bool = True,
    keyboard: bool = True,
    midi: bool = True,
    mouse: bool = True,
    nkro: bool = True,
    )