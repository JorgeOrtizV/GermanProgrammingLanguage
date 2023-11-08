["abfolge", 
    ["setzen", "Shape", ["dict", ["_classname", "_name", "_thing", "_weight", "_density"], ["Shape", "None", "None", "None", "None"]]],
    ["setzen", "square_new", ["funktion", ["name"], 
        ["abfolge",
            ["setzen", "shape_obj", ["abrufen", "Shape"]],
            ["set_dict", ["abrufen", "shape_obj"], "_name", ["abrufen","name"]],
            ["print", ["abrufen", "shape_obj"]],
            ["abrufen", "shape_obj"]
            ]
        ]
    ],
    ["setzen", "myShape", ["aufrufen", "square_new", "Circle"]]


]