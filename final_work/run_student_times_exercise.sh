cd student_times
cat student_test_posts.csv | ./student_times_mapper.py | sort | ./student_times_reducer.py
