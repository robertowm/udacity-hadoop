cd popular_tags
cat student_test_posts.csv | ./popular_tags_mapper.py | sort | ./popular_tags_reducer.py
