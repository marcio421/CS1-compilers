program_0 = """class A { };"""

program_1 = """
        class A {
          
        };
"""

program_2 = """class A2I {

     c2i(char : String) : Int {
	if char = "0" then 0 else
	if char = "1" then 1 else
	if char = "2" then 2 else
        if char = "3" then 3 else
        if char = "4" then 4 else
        if char = "5" then 5 else
        if char = "6" then 6 else
        if char = "7" then 7 else
        if char = "8" then 8 else
        if char = "9" then 9 else
        { abort(); 0; }
        fi fi fi fi fi fi fi fi fi fi
     };"""

program_4 = """class A {
    Bool X = true;
    Bool Y = false;
    return
};"""

program_5 = """
        class A {
            return "12345"           
        };
"""


program_6 = """
        class A {
            sum () : Int {
                1 + 1
            };
        }
"""

# list of classes

program_7 = """
        class A {
            a_two : Int <- 1 + 1;
        }

        class B {
            b_two: Int <- 1 + 1;
        }

"""

# class with inheritance


program_8 = """
        class A {
            x : Int <- 1 + 1;
        }

        class B inherits A {
            y : Int <- 1 + 1;
        }

"""

# class with more then one expression


program_9 = """
        class A {
            x : Int <- 1 + 1;
            y : Int <- 2 + 2;
        }

        class B inherits A {
            x: Int <- 1 + 1;
        }

"""

# class with attr declarations

program_10 = """
        class A {
            a: Int <- 1 + 1;
        }

        class B inherits A {
            age : Int;
            name : String;
            two : Int <- 2 + 2;
        }

"""

program_11 = """
    class C {
        age : Int <- 24;
    }
"""

program_12 = """
    class A {
        get_age () : Int {
            24
        };
    }
"""

program_13 = """
    class Function {
        sum (x: Int, y: Int) : Int {
            2*x - y/2 + 100
        };
    }
"""

program_14 = """
    class A {
        max ( x: Int, y: Int) : Int {
            if y <= x
            then
                x
            else
                y
            fi
        };
    }
"""

current_developing = program_14

test_programs = {
    "single_arith_class": program_6,
    "list_arith_classes": program_7,
    "list_inheritance_classes": program_8,
    "class_many_expressions": program_9,
    "attributes_declaration": program_10,
    "attr_assignment": program_11,
    "method_declaration": program_12,
    "method_with_params": program_13,
    "conditional_if": program_14
}
