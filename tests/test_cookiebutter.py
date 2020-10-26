import subprocess


def test_cookiebutter():
    # Arrange
    expected = "hello"

    # Act
    subprocess.run("cookiebutter -f --no-input .")

    with open("./folder.gen/text.txt") as f:
        result = f.read()

    # Assert
    assert expected == result
