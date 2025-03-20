# college = {
#     "user1": {
#         'name': "aashish",
#         'class': "BCA",
#         'college' : "FIT College, Meerut",
#         "subject" :{
#             '1':"CS",
#             '2':"POM"
#         }
#     },
#     "user2" : {
#         'name' : "Sahil",
#         'class': "BBA",
#         'college' : "FIT College",
#         "subject" :{
#             '1':"CS",
#             '2':"POM"
#         }

#     }
# }

# for a, b in college.items():
#     print(f"{a}")
#     for a, b in b.items():
#         print(f"{b}")

a = {
    "student1": {
        "name": "aashish",
        "Age": 19,
        "subject": {
            "Hindi": 79,
            "English": 80
        }
    },
    "student2": {
        "name": "Sahil",
        "Age": 21,
        "subject": {
            "Hindi": 89,
            "English": 90
        }
    }
}

for student_key, student_value in a.items():
    print(f"{student_key}")
    for info_key, info_value in student_value.items():
        if info_key == "subject":
            print(info_key)
            for subject_key, subject_value in info_value.items():
                print(f"{subject_key}: {subject_value}")
        else:
             print(f"{info_key}: {info_value}")
             