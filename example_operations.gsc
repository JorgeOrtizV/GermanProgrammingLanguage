["abfolge",
        ["multiplication", 2, 2], 

        ["division", 8, 2],

        ["power", 3, 2],
        ["print", ["addieren", ["multiplication", 5, 5], ["division", 15, 3]]],

        ["setzen", "myarray", ["array", 5]],
        ["get_array", ["abrufen", "myarray"], 3],
        ["set_array", ["abrufen", "myarray"], 3, 5],
        ["print", ["abrufen", "myarray"]],

        ["setzen", "dictionary_1",
                        ["dict", "dictionary_1"]],
                                ["set_dict", "dictionary_1", 1, 3],
                                        ["get_dict", "dictionary_1", 1],
        ["setzen","dictionary_2" ,     
                        ["dict", "dictionary_2"]],
                                ["set_dict", "dictionary_2", 1, 4],
                                        ["get_dict", "dictionary_2", 1],

        ["setzen",["merge_dict", "dictionary", "dictionary_1", "dictionary_2"]],




]

