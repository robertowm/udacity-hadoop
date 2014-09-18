cd average_length
cat student_test_posts.csv | ./average_length_mapper.py | sort | ./average_length_reducer.py
