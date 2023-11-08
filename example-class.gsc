["abfolge", 
    ["setzen", "Shape", ["dict", ["_classname", "_name", "_thing", "_weight", "_density"], ["Shape", "None", "None", "None", "None"]]],
    ["setzen", "square_new", ["funktion", ["name"], 
        ["abfolge",
            ["setzen", "shape_obj", ["abrufen", "Shape"]],
            ["set_dict", ["abrufen", "shape_obj"], "_name", ["abrufen","name"]],
            ["abrufen", "shape_obj"]
            ]
        ]
    ],
    ["setzen", "myShape", ["aufrufen", "square_new", "Circle"]],

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
    ["setzen", "myShape", ["aufrufen", "shape_density", 3, 3]]
]