import numpy as np

image = np.random.randint(0, 256, size=(10,10)) # Create a random RGB image of size 10x10
print("\n",image)

print(f"\n Image stats")
print(f"\n brightness: {np.mean(image)}")
print(f"\n contrast: {np.std(image)}")

# For increase in brightness we add to constant
brighter=np.clip(image + 50, 0 ,255)
print(f'\n brightness increased by {np.mean(brighter):.2f}')

contrast=np.clip(image * 50, 0, 255)
print(f'\n contrast increased by {np.std(contrast):.2f} \n')