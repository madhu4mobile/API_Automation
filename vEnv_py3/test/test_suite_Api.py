import pprint
from woocommerce import API


def test_printing_response():
    wcapi = API(
        url="http://localhost:10004",
        consumer_key="ck_a29265ef5bc096bd7cec4266a7732ff63463521a",
        consumer_secret="cs_4ac296939dcd86e2aef8b541b9f1c2ad8582a93b",
        version="wc/v3"
    )

    r = wcapi.get("users")

    pprint.pprint(r.json())


def test_this_is_second(x=1, y=1):
    print(x*y)


test_this_is_second(x=2, y=7)
