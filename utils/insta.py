import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Example post URL
post_url = 'https://www.instagram.com/reel/DDE5wwQNGTN/?igsh=Z3N3Y3NoM2Z4OTV3'

# Extract shortcode from the URL
shortcode = post_url.strip('/').split('/')[-1]

# Download the post (video or image)
post = instaloader.Post.from_shortcode(L.context, shortcode)
L.download_post(post, target=post.owner_username)
