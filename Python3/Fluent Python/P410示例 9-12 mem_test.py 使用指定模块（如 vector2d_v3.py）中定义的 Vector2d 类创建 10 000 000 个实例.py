$ time python3 mem_test.py vector2d_v3.py
Selected Vector2d type: vector2d_v3.Vector2d
Creating 10,000,000 Vector2d instances
Initial RAM usage: 5,623,808
Final RAM usage: 1,558,482,944
real 0m16.721s
user 0m15.568s
sys 0m1.149s
$ time python3 mem_test.py vector2d_v3_slots.py
Selected Vector2d type: vector2d_v3_slots.Vector2d
Creating 10,000,000 Vector2d instances
Initial RAM usage: 5,718,016
Final RAM usage: 655,466,496
real 0m13.605s
user 0m13.163s
sys 0m0.434s