def check_triangle(a, b, c):
    # Check if it satisfies the triangle inequality theorem
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


if __name__ == "__main__":
    # Input from user
    side_a = int(input("Enter the length of side a: "))
    side_b = int(input("Enter the length of side b: "))
    side_c = int(input("Enter the length of side c: "))

    if check_triangle(side_a, side_b, side_c):
        print("Possible triangle")
    else:
        print("Impossible triangle")
