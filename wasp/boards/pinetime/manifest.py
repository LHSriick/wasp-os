freeze('../..',
    (
        'boot.py',
        'clock.py',
        'demo.py',
        'drivers/battery.py',
        'drivers/nrf_rtc.py',
        'drivers/signal.py',
        'drivers/st7789.py',
        'drivers/vibrator.py',
        'fonts.py',
        'main.py',
        'manager.py',
        'logo.py',
    ),
    opt=3
)
freeze('.', 'watch.py', opt=3)
