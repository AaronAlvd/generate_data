import uuid
import data.user_id as user_id
import data.captions as captions
import data.first_name as first_name
import data.last_name as last_name
import data.imageLinks as links
import data.imageLinks2 as links2
import data.comments.comments as comments
import data.comments.comments2 as comments2
import data.comments.comments3 as comments3
import data.comments.comments4 as comments4
import data.comments.comments5 as comments5
import data.comments.comments6 as comments6
import data.comments.comments7 as comments7
import data.comments.comments8 as comments8
import data.comments.comments9 as comments9
import data.comments.comments10 as comments10
import data.comments.comments11 as comments11
import data.comments.comments12 as comments12
import data.post_id as post_id
import random
import data.bio as bio

userId = user_id.data
captions = captions.captions
first_names = first_name.first_names
last_names = last_name.last_names
imageLinks = links.imageLinks + links2.imageLinks2
posts_id = post_id.posts_id
bios = bio.bios
combined_comments = (
    comments.comments + comments2.comments2 + comments3.comments3 + comments4.comments4 + comments5.comments5 +
    comments6.comments6 + comments7.comments7 + comments8.comments8 + comments9.comments9 + comments10.comments10 +
    comments11.comments11 + comments12.comments12
)

def seedPosts(): 
  with open('./seedData/posts.js', 'w') as file:
        # Start the array in the JS file
        file.write('const posts05 = [\n')

        current_user = 0
        current_caption = 0
        
        array = ['const posts05_id = [\n']
        
        for i in range(10000):  # Generate x posts
            # Generate a new UUID for each post
            id = uuid.uuid4()
            
            array.append('  { ' + f" postId: '{id}' " + '}, \n')
                
            # Write the post object
            file.write('  {\n')
            file.write(f"    id: '{id}',\n")
            file.write(f"    userId: '{userId[current_user]['id']}',\n")
            file.write(f'    groupId: "default",\n')
            file.write(f'    caption: "{captions[current_caption]}",\n')
            file.write(f"    photo: '{imageLinks[random.randint(0, 47999)]}',\n")
            file.write('  },\n')
            
            # Cycle through userId and captions arrays
            current_user = (current_user + 1) % len(userId)
            current_caption = (current_caption + 1) % len(captions)
        
        # End the array in the JS file
        array.append(']')
        
        with open('./seedData/postIds.js', 'w') as file2:
            file2.writelines(array)
        
        file.write(']\n')

def seedUsers():
 with open('./seedData/users.js', 'w') as file:
        # Start of the array in the JS file
        array = ['const seedData = [\n']
        array2 = ['const data = [\n']
        
        # Iterate over the number of users to generate (e.g., 10)
        for i in range(10000):  # Generate 10 users (adjust as needed)
            current = 0
            id = uuid.uuid4()  # Generate unique UUID for each user
            
            # Start of user object
            array.append('  { \n')
            array2.append('    {' + f" id: '{id}' " + '}, \n')
            
            # Add user properties to the array
            while current < 9:
                if current == 0:
                    array.append(f"    id: '{id}', \n")  # Add the UUID
                elif current == 1:
                    current_firstName = first_names[random.randint(0, len(first_names) - 1)]
                    array.append(f'    firstName: "{current_firstName}", \n')  # Random first name
                elif current == 2:
                    current_lastName = last_names[random.randint(0, len(last_names) - 1)]
                    array.append(f'    lastName: "{current_lastName}", \n')  # Random last name
                elif current == 3:
                    randomNum = random.randint(999, 99999)
                    array.append(f'    username: "{current_firstName}{current_lastName}{randomNum}", \n')  # Username
                elif current == 4:
                    array.append(f'    email: "{current_firstName}{current_lastName}{randomNum}@gmail.com", \n')  # Email
                elif current == 5:
                    array.append(f"    password: 'password', \n")  # Password placeholder
                elif current == 6:
                    randomBio = bios[random.randint(0, len(bios) - 1)]  # Random bio
                    array.append(f'    bio: "{randomBio}", \n')
                elif current == 7:
                    array.append("    profilePhoto: null, \n")  # Profile photo (null for now)
                elif current == 8:
                    array.append("  }, \n")  # Closing the user object

                current += 1  # Increment the state to move to the next property

        # End of the array in the JS file
        array.append(']\n')
        array2.append(']\n')
        
        with open('./seedData/userIds.js', 'w') as file2:
            file2.writelines(array2)
        
        # Write the array to the file
        file.writelines(array)

def seedComments(num, num2): 
    with open(f'./seedData/comments/comments{num}.js', 'w') as file:
        # Start the array in the JS file
        file.write(f'const comments{num} = [\n')
        
        array = [None] * num2
        
        for i in range(num2):  # Generate x posts
            # Generate a new UUID for each post
            id = uuid.uuid4()
            
            array[i] = ('  { ' + f" commentId: '{id}' " + '}, \n')
                
            # Write the post object
            file.write('  {\n')
            file.write(f"    id: '{id}',\n")
            file.write(f"    userId: '{userId[random.randint(0, len(userId))]['id']}',\n")
            file.write(f"    postId: '{posts_id[random.randint(0, len(posts_id))]['postId']}',\n")
            file.write(f'    comment: "{combined_comments[random.randint(0, len(combined_comments))]}",\n')
            file.write('  },\n')
        
        file.write(']\n')
        return array       

def updateUsers():
    with open('./seedData/users.js', 'r') as file:
        lines = file.readlines()
        
    for i in range(50009, 100001, 10):
        lines[i] = f"    profilePhoto: '{imageLinks[random.randint(0, 47999)]}' \n"
        
    with open('./updatedUser02.js', 'w') as file2:
        file2.writelines(lines[50001:100002])

def runSeedComments(): 
    array = []

    for i in range(5):
        retVal = seedComments(i, 5)
        
runSeedComments()