["abfolge", 
    ["setzen", "Shape", ["dict", ["_classname", "_name", "_weight", "_density", "_shape_density"], ["Shape", "None", "None", "None", "None"]]],
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
            ["set_dict", ["abrufen", "myShape"], "_weight", ["abrufen","weight"]],
            ["set_dict", ["abrufen", "myShape"], "_density", ["division",["abrufen","weight"],["abrufen","thing"]]],
            ["get_dict", ["abrufen", "myShape"], "_density"]
            ]
        ]
    ],
    ["set_dict", ["abrufen", "Shape"], "_shape_density", ["abrufen", "shape_density"]],

    ["setzen", "myShape", ["aufrufen", "shape_new", "Circle"]],


    ["setzen", "Square", ["dict", ["_classname", "name", "side", "area", "square_area", "parent"], ["Square", "None", "None", "None", "None", ["abrufen", "Shape"]]]],
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
            ["set_dict", ["abrufen", "mySquare"], "area", ["multiplication",["abrufen","thing"],["abrufen","thing"]]],
            ["abrufen", "mySquare"]
            ]
        ]
    ],
    ["set_dict", ["abrufen", "Square"], "square_area", ["abrufen", "square_area"]],

    ["setzen", "mySquare", ["aufrufen", "square_new", "sq", 3]],
    ["setzen", "mySquare", ["method", ["get_dict", ["abrufen", "mySquare"], "square_area"], ["get_dict", ["abrufen", "mySquare"], "side"]]],



    ["setzen", "Circle", ["dict", ["_classname", "name", "radius", "area", "circle_area", "parent"], ["Circle", "None", "None", "None", "None", ["abrufen", "Shape"]]]],
    ["setzen", "circle_new", ["funktion", ["name", "radius"], 
        ["abfolge",
            ["setzen", "shape_obj", ["abrufen", "Circle"]],
            ["set_dict", ["abrufen", "shape_obj"], "radius", ["abrufen","radius"]],
            ["set_dict", ["abrufen", "shape_obj"], "name", ["abrufen","name"]],
            ["abrufen", "shape_obj"]
            ]
        ]
    ],
    ["setzen", "circle_area", ["funktion", ["thing"],
        ["abfolge",
            ["set_dict", ["abrufen", "myCircle"], "area", ["multiplication",["power", ["abrufen","thing"], 2],3.14]],
            ["abrufen", "myCircle"]
            ]
        ]
    ],
    ["set_dict", ["abrufen", "Circle"], "circle_area", ["abrufen", "circle_area"]],

    ["setzen", "myCircle", ["aufrufen", "circle_new", "ci", 2]],
    ["setzen", "myCircle", ["method", ["get_dict", ["abrufen", "myCircle"], "circle_area"], ["get_dict", ["abrufen", "myCircle"], "radius"]]],

    ["addieren", ["method", ["get_dict", ["get_dict", ["abrufen", "mySquare"], "parent"], "_shape_density"], ["get_dict", ["abrufen", "mySquare"], "area"], 5], ["method", ["get_dict", ["get_dict", ["abrufen", "myCircle"], "parent"], "_shape_density"], ["get_dict", ["abrufen", "myCircle"], "area"], 5]]

]