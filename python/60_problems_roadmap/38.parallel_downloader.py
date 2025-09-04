"""
Problem:
    You are given a list of image URLs. Download them in parallel using threads and save them to disk with unique names.
"""


import time
import concurrent.futures
import requests
import os

def save_imgs(data):

    index, img_url = data
    os.makedirs("unsplash_images", exist_ok=True)

    try:
        response = requests.get(f'{img_url}', timeout=10) # Adding timeout=10 makes sure that any single request won't wait forever.
        # img_name = img_url.split('/')[3] + ".png"
        img_name = f"image-{index}.jpg"

        with open(f'unsplash_images/{img_name}', 'wb') as f:
            f.write(response.content)
        
        print(f"{img_name} downloaded")
                        
    except Exception as e:
        print(f"Error with {img_name} : {e}")


img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start_time = time.perf_counter()

# thread = threading.Thread(target=save_imgs, args=[img_urls])
# thread.start()
# thread.join()
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executer:
    executer.map(save_imgs, enumerate(img_urls))

end_time = time.perf_counter()

print(f'Total time is {end_time - start_time:.2f}')  


# without multithreading : Total time is 37.53
# with multithreading : Total time is 29.53