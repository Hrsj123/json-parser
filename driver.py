from json_parser import check_json

# string = '[]'
# string = '[1, 2, 3, "hello"]'
# string = '[[true, false], null, "world"]'
# string = '[1.23, 4.56, -7.89]'
# string = '["string", "with", "escaped\\ncharacters"]'
# string = '[[[100]], [[200, 300]]]'
# string = '[true, true, false, false]'
# string = '[null, null, null]'
# string = '[1000000000000, -999999999999]'
# string = '[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]'
#
# string = '''[1, 2, 3, ,]'''
# string = '''[1 2 3]'''
# string = '''"unterminated\nstring"'''
# string = '''[array]'''
# string = '''[true, "hello", missingValue]'''
# string = '''[[1, 2], [3, 4, "unclosed string"]'''
# string = '''[100, true, "hello", Infinity]'''
# string = '''[100, true, "hello", NaN]'''
# string = '''[function(){}]'''
# string = '''[[[1, 2], [3, 4]], [5, 6, , 7]]'''
# string = '''["string", 'also a string']'''
# string = '''[   ]'''
# string = '''[1, , , , ]'''


# string = '''{"name": "Alice", "age": 30}'''
# string = '''{"fruits": ["apple", "banana", "orange"], "color": "red"}'''
# string = '''{"active": true, "score": 4.25}'''
# string = '''{}'''
# string = '''{"nested": {"key": "value"}}'''
# string = '''{"array": [1, 2, 3]}'''
# string = '''{"null_value": null}'''
# string = '''{"date": "2024-06-25"}'''
# string = '''{"key_with_spaces": "value with spaces"}'''
# string = '''{"unicode_key": "\\u00A9 Copyright"}'''
#
# string = '''{name: "Alice"}'''
# string = '''{"name": "Alice",}'''
# string = '''{"name",: "Alice",}'''
# string = '''{"name":, "Alice"}'''
# string = '''{"name",: "Alice",}'''
# string = '''{"key": value}'''
# string = '''{"key1", "key2"}'''
# string = '''"key": "value", "another key"'''
# string = '''{"key": [1, 2, 3], 4}'''
# string = '''{"key": function(){}}'''

string = """
{
    "data": {
        "items": [
            {
                "id": 1,
                "name": "Product A",
                "details": {
                    "description": "This is a great product.",
                    "specifications": {
                        "weight": 2.5,
                        "dimensions": {
                            "width": 10,
                            "height": 15,
                            "depth": 5
                    },
                    "features": [
                        "Feature 1",
                        "Feature 2",
                        {
                            "sub_feature": "Advanced Feature",
                            "details": "This sub-feature provides additional functionality."
                        }
                    ]
                },
                "reviews": [
                    {
                        "author": "John Doe",
                        "rating": 5,
                        "comment": "Excellent product!"
                    },
                    {
                        "author": "Jane Smith",
                        "rating": 4,
                        "comment": "Good product, but slightly expensive."
                    }
                ]
                }
            },
            {
                "id": 2,
                "name": "Product B",
                "details": {
                    "description": "Another great product from the same brand.",
                    "related_items": [
                        {
                            "id": 1,
                            "reference": "This relates back to Product A."
                        },
                        {
                            "id": 3,
                            "reference": "Another related product not shown here."
                        }
                    ]
                }
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 5
        }
    },
    "meta": {
        "generated_at": "2024-06-25T09:08:00Z",
        "version": 1.0
    }
}
"""
string = r"""
[
    "JSON Test Pattern pass1",
    {"object with 1 member":["array with 1 element"]},
    {},
    [],
    -42,
    true,
    false,
    null,
    {
        "integer": 1234567890,
        "real": -9876.543210,
        "e": 0.123456789e-12,
        "E": 1.234567890E+34,
        "":  23456789012E66,
        "zero": 0,
        "one": 1,
        "space": " ",
        "quote": "\"",
        "backslash": "\\",
        "controls": "\b\f\n\r\t",
        "slash": "/ & \/",
        "alpha": "abcdefghijklmnopqrstuvwyz",
        "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
        "digit": "0123456789",
        "0123456789": "digit",
        "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
        "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
        "true": true,
        "false": false,
        "null": null,
        "array":[  ],
        "object":{  },
        "address": "50 St. James Street",
        "url": "http://www.JSON.org/",
        "comment": "// /* <!-- --",
        "# -- --> */": " ",
        " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
        "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
        "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
        "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string"
    },
    0.5 ,98.6
,
99.44
,

1066,
1e1,
0.1e1,
1e-1,
1e00,2e+00,2e-00
,"rosebud"]
"""

check_json(string)
