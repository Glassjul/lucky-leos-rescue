# Accuracy test for the breed filter.
# For every breed in the Breed filter, check that the filtered list has:
#   - 0 missing: every dog of that breed is shown
#   - 0 extra: no dog of a different breed is shown

from dogs import DOGS, BREEDS
from filters import filter_by_breed

all_passed = True

print("Breed                      Shown  Missing  Extra  Result")
print("-------------------------  -----  -------  -----  ------")

for breed in BREEDS:
    # What the filter returns
    shown = filter_by_breed(DOGS, breed)

    # What it should return: every dog in the data with this exact breed
    expected = []
    for dog in DOGS:
        if dog["breed"] == breed:
            expected.append(dog)

    # Count dogs that should be shown but are not
    missing = 0
    for dog in expected:
        if dog not in shown:
            missing = missing + 1

    # Count dogs that are shown but are a different breed
    extra = 0
    for dog in shown:
        if dog["breed"] != breed:
            extra = extra + 1

    if missing == 0 and extra == 0:
        result = "PASS"
    else:
        result = "FAIL"
        all_passed = False

    print(f"{breed:<25}  {len(shown):>5}  {missing:>7}  {extra:>5}  {result}")

print()
if all_passed:
    print("All breeds passed: 0 missing, 0 extra.")
else:
    print("At least one breed failed.")