["abfolge", 
    ["setzen", "Shape", ["dict", ["_classname", "_name", "_thing", "_weight", "_density", "_shape_density"], ["Shape", "None", "None", "None", "None", "None"]]],
    ["setzen", "shape_new", ["funktion", ["name"], 
        ["abfolge",
            ["setzen", "shape_obj", ["abrufen", "Shape"]],
            ["set_dict", ["abrufen", "shape_obj"], "_name", ["abrufen","name"]],
            ["abrufen", "shape_obj"]
            ]
        ]
    ],

    ["setzen", "shape_density", ["funktion", ["thing", "weight"],
        ["abfolge",
            ["set_dict", ["abrufen", "myShape"], "_thing", ["abrufen","thing"]],
            ["set_dict", ["abrufen", "myShape"], "_weight", ["abrufen","weight"]],
            ["set_dict", ["abrufen", "myShape"], "_density", ["multiplication",["abrufen","thing"],["abrufen","weight"]]],
            ["get_dict", ["abrufen", "myShape"], "_density"],
            ["abrufen", "myShape"]
            ]
        ]
    ],
    ["set_dict", ["abrufen", "Shape"], "_shape_density", ["abrufen", "shape_density"]],

    ["setzen", "myShape", ["aufrufen", "shape_new", "Circle"]],

    ["setzen", "myShape", ["method", ["get_dict", ["abrufen", "myShape"], "_shape_density"], 3, 3]],



    ["setzen", "Square", ["dict", ["_classname", "name", "side", "square_area", "parent"], ["Square", "None", "None", "None", ["abrufen", "Shape"]]]],
    ["setzen", "square_new", ["funktion", ["name", "side"], 
        ["abfolge",
            ["setzen", "shape_obj", ["abrufen", "Square"]],
            ["set_dict", ["abrufen", "shape_obj"], "side", ["abrufen","side"]],
            ["set_dict", ["abrufen", "shape_obj"], "name", ["abrufen","name"]],
            ["abrufen", "shape_obj"]
            ]
        ]
    ],
    ["setzen", "square_area", ["funktion", ["thing"],
        ["abfolge",
            ["set_dict", ["abrufen", "myShape"], "square_area", ["multiplication",["abrufen","thing"],["abrufen","thing"]]],
            ["abrufen", "mySquare"]
            ]
        ]
    ],
    ["set_dict", ["abrufen", "Square"], "square_area", ["abrufen", "square_area"]],

    ["setzen", "mySquare", ["aufrufen", "square_new", "Square", 5]],
    ["setzen", "mySquare", ["method", ["get_dict", ["abrufen", "mySquare"], "square_area"], ["get_dict", ["abrufen", "mySquare"], "side"]]]

]