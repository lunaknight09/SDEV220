#Nathan Hopkins
#Data Class for Computer Parts Import
#Jan 31, 2023


from CustomGamingComputerBuild import CustomGamingComputerBuild

# Instantiate two unique instances of CustomGamingComputerBuild
computer_build1 = CustomGamingComputerBuild("Intel Core i9", "NVIDIA GeForce RTX 3080", "32GB", "1TB SSD")
computer_build2 = CustomGamingComputerBuild("AMD Ryzen 7", "AMD Radeon RX 6800 XT", "16GB", "2TB HDD")

# Print the instances to the console
print(computer_build1)
print(computer_build2)

# Test equality between instances
if computer_build1 == computer_build2:
    print("The computer builds are identical.")
else:
    print("The computer builds are different.")
