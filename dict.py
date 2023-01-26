sectors = {
    range(0, 60000): 'MB1',
    range(60000, 170001): 'MB2',
    range(170000, 400001): 'MB3',
    range(400000, 600001): 'CB1',
    range(600000, 800001): 'CB2',
    range(800000, 1000001): 'CB3',
    range(1000000, 7000001): 'KB1',
    range(7000000, 260000001): 'KB2',
    'last': 'KB3',

}

tables_with_sectors = {
    100: {
        'x11': {
            'MB1MB2MB3': {
                range(20, 30): 20,
                range(30, 40): 30,
                range(0, 20): 10,
                range(40, 50): 40,
                range(50, 60): 50,
                range(60, 70): 60,
                range(70, 80): 70,
                range(80, 90): 80,
                range(90, 100): 90

            },
            'CB1CB2CB3': {
                range(0, 20): 0,
                range(20, 30): 15,
                range(30, 40): 30,
                range(40, 50): 40,
                range(50, 60): 50,
                range(60, 70): 60,
                range(70, 80): 70,
                range(80, 90): 80,
                range(90, 100): 90

            },
            'KB1KB2KB3': {
                range(0, 20): 0,
                range(20, 30): 5,
                range(30, 40): 15,
                range(40, 50): 20,
                range(50, 60): 40,
                range(60, 70): 60,
                range(70, 80): 70,
                range(80, 90): 80,
                range(90, 100): 90

            }

        },
        'x21': {
            'MB1': {
                range(0, 300): 0,
                range(300, 600): 15,
                range(600, 900): 30,
                range(900, 1200): 60,
                range(1200, 1500): 70,
                range(1500, 1800): 80,
                range(1800, 2100): 90

            },
            'MB2': {
                range(0, 300): 0,
                range(300, 600): 15,
                range(600, 900): 30,
                range(900, 1200): 45,
                range(1200, 1500): 60,
                range(1500, 1800): 70,
                range(1800, 2100): 80,
                range(1800, 2100): 90

            },
            'MB3': {
                range(0, 300): 0,
                range(300, 600): 15,
                range(600, 900): 30,
                range(900, 1200): 45,
                range(1200, 1500): 60,
                range(1500, 1800): 75,
                range(1800, 2100): 85,
                range(1800, 2100): 90,
                range(1800, 2100): 95

            },
            'CB1CB2CB3': {
                range(0, 300): 0,
                range(300, 600): 12,
                range(600, 900): 23,
                range(900, 1200): 34,
                range(1200, 1500): 45,
                range(1500, 1800): 56,
                range(1800, 2100): 67,
                range(1800, 2100): 78,
                range(1800, 2100): 89

            },
            'KB1KB2KB3': {
                range(0, 900): 0,
                range(900, 1200): 15,
                range(1200, 1500): 30,
                range(1500, 1800): 45,
                range(1800, 2100): 60,
                range(1800, 2100): 75,
                range(1800, 2100): 90

            }



        }

    },
    0: {
        'x12': {
            'MB1MB2MB3': {
                range(0, 150): 100,
                range(150, 250): 90,
                range(250, 300): 75,
                range(300, 350): 60,
                range(350, 400): 45,
                range(400, 450): 30,
                range(450, 500): 15

            },
            'CB1CB2CB3': {
                range(0, 100): 100,
                range(100, 150): 85,
                range(150, 250): 70,
                range(250, 300): 65,
                range(300, 350): 50,
                range(350, 400): 35,
                range(400, 450): 20,
                range(450, 500): 5

            },
            'KB1KB2KB3': {
                range(0, 50): 100,
                range(50, 100): 89,
                range(100, 150): 78,
                range(150, 250): 67,
                range(250, 300): 56,
                range(300, 350): 45,
                range(350, 400): 34,
                range(400, 450): 23,
                range(450, 500): 12

            }

        }

    }
}






KBx21 = {
    range(0, 900): 0,
    range(900, 1200): 15,
    range(1200, 1500): 30,
    range(1500, 1800): 45,
    range(1800, 2100): 60,
    range(1800, 2100): 75,
    range(1800, 2100): 90,
    'last': 100,
    'key': 'KB1KB2KB3'

}

b5 = {
    range(0, 100): 100,
    range(100, 146): 89,
    range(146, 196): 78,
    range(196, 246): 67,
    range(246, 296): 56,
    range(296, 346): 45,
    range(346, 396): 34,
    range(396, 446): 23,
    range(446, 500): 12,
    'last': 0,

}

MB1MB2x23 = {
    range(0, 100): 0,
    range(100, 150): 15,
    range(150, 200): 30,
    range(200, 250): 45,
    range(250, 300): 60,
    range(300, 350): 75,
    range(350, 400): 90,
    'last': 100,
    'key': 'MB1MB2'

}

MB3x23 = {
    range(0, 100): 0,
    range(100, 150): 10,
    range(150, 200): 20,
    range(200, 250): 30,
    range(250, 300): 40,
    range(300, 350): 50,
    range(350, 400): 60,
    range(400, 450): 75,
    range(450, 500): 90,
    'last': 100,
    'key': 'MB3'

}

CBx23 = {
    range(0, 150): 0,
    range(150, 200): 5,
    range(200, 250): 10,
    range(250, 300): 25,
    range(300, 350): 40,
    range(350, 400): 55,
    range(400, 450): 70,
    range(450, 500): 85,
    'last': 100,
    'key': 'CB1CB2CB3'

}

KBx23 = {
    range(0, 200): 0,
    range(200, 250): 5,
    range(250, 300): 20,
    range(300, 350): 35,
    range(350, 400): 50,
    range(400, 450): 65,
    range(450, 500): 80,
    'last': 100,
    'key': 'KB1KB2KB3'

}

b7 = {
    range(0, 10): 0,
    range(10, 20): 12,
    range(20, 30): 23,
    range(30, 40): 34,
    range(40, 50): 45,
    range(50, 60): 56,
    range(60, 70): 67,
    range(70, 80): 78,
    range(80, 90): 89,
    'last': 100

}

b8 = {
    range(0, 12): 0,
    range(12, 23): 12,
    range(23, 34): 23,
    range(34, 45): 34,
    range(45, 56): 45,
    range(56, 67): 56,
    range(67, 78): 67,
    range(78, 89): 78,
    range(89, 100): 89,
    'last': 100

}

b11 = {
    range(0, 6): 0,
    range(6, 9): 12,
    range(9, 12): 23,
    range(12, 15): 34,
    range(15, 18): 45,
    range(18, 21): 56,
    range(21, 24): 67,
    range(24, 27): 78,
    range(27, 30): 89,
    'last': 100

}

b12 = {
    range(0, 6): 100,
    range(6, 9): 89,
    range(9, 12): 78,
    range(12, 15): 67,
    range(15, 18): 56,
    range(18, 21): 45,
    range(21, 24): 34,
    range(24, 27): 23,
    range(27, 30): 12,
    'last': 0

}

b13 = {
    range(0, 2): 100,
    range(2, 4): 89,
    range(4, 6): 78,
    range(6, 8): 67,
    range(8, 10): 56,
    range(10, 12): 45,
    range(12, 14): 34,
    range(14, 16): 23,
    range(16, 18): 12,
    'last': 0

}

b14 = {
    range(0, 5): 100,
    range(5, 10): 89,
    range(10, 20): 78,
    range(20, 30): 67,
    range(30, 40): 56,
    range(40, 50): 45,
    range(50, 60): 34,
    range(60, 70): 23,
    range(70, 80): 12,
    'last': 0

}
