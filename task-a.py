import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Tulip.jpg')

# convert to RGB
img_org = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Split channels
b_channel, g_channel, r_channel = cv2.split(img)


plt.figure(figsize=(10, 12))
plt.subplot(2,2,1)
plt.imshow(img_org, cmap='gray')
plt.title('ORG_Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(b_channel, cmap='gray')
plt.title('Blue_Channel')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(g_channel, cmap='gray')
plt.title('Green_Channel')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(r_channel, cmap='gray')
plt.title('Red_Channel')
plt.axis('off')

plt.savefig('all_channels.png', dpi=300, bbox_inches='tight')

# plt.show()



