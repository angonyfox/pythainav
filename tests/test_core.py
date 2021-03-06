import pythainav as nav


def test_get_nav():
    kt_nav = nav.get("KT-PRECIOUS")
    print(kt_nav)
    assert kt_nav.value >= 0


def test_get_nav_with_date():
    kt_nav = nav.get("KT-PRECIOUS", date="1 week ago")
    print(kt_nav)
    assert kt_nav.value >= 0


def test_get_all():
    kt_navs = nav.get_all("KT-PRECIOUS")
    print(kt_navs)
    assert len(kt_navs) >= 0


def test_get_all_pandas():
    import pandas as pd

    df = nav.get_all("KT-PRECIOUS", asDataFrame=True)
    assert isinstance(df, pd.DataFrame)
