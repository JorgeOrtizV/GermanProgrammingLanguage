["abfolge",
        ["multiplication", 2, 2], 

        ["division", 8, 2],

        ["power", 3, 2],
        ["print", ["addieren", ["multiplication", 5, 5], ["division", 15, 3]]],

        ["setzen", "myarray", ["array", 5]],
        ["get_array", ["abrufen", "myarray"], 3],
        ["set_array", ["abrufen", "myarray"], 3, 5],
        ["print", ["abrufen", "myarray"]],

        ["setzen", "mydict", ["dict", ["key1", "key2"], [1, 2]]],
        ["get_dict", ["abrufen", "mydict"], "key1"],
        ["set_dict", ["abrufen", "mydict"], "key2", 20],
        ["print", ["abrufen", "mydict"]],
        ["setzen", "mydict2", ["dict", ["key3", "key4"], [5, 6]]],
        ["merge_dict", "newdict", ["abrufen", "mydict"], ["abrufen", "mydict2"]]
]

