cd study_groups
cat student_test_posts.csv | ./study_groups_mapper.py | sort | ./study_groups_reducer.py
