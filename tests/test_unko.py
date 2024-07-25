from unko import deru


def test_deru(capsys):
    deru()
    assert capsys.readouterr().out == "puripuri\n"
