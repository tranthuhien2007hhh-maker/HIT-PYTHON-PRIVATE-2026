scores = [8, 4, 9, 5]
average_score=sum(scores)/len(scores)
threshold=5
count =0
for score in scores:
    if score >= threshold:
        count += 1
        # return count
print(f"so diem lon hon 5 : {count}")