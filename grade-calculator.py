def average(marks):
    """Return the average of a list of marks."""
    if not marks:
        raise ValueError("marks list cannot be empty")
    return sum(marks) / len(marks)
def grade(avg):
    """Return a letter grade for an average."""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    return "F"
def is_pass(marks, pass_mark=40):
    """Student passes only if every subject is >= pass_mark."""
    return all(m >= pass_mark for m in marks)
def main():
    name = input("Student name: ")
    n = int(input("Number of subjects: "))
    marks = [float(input(f"Marks in subject {i + 1}: ")) for i in range(n)]
    avg = average(marks)
    print(f"\nStudent : {name}")
    print(f"Average : {avg:.2f}")
    print(f"Grade   : {grade(avg)}")
    print(f"Result  : {'PASS' if is_pass(marks) else 'FAIL'}")
if __name__ == "__main__":
    main()