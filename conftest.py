import os

import pytest
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir="reports"
    os.makedirs(report_dir,exist_ok=True)
    now=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    config.option.htmlpath=f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("\nstarting")
    yield
    print("\nEnd")




