import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.ransomlook.io/groups")
soup = BeautifulSoup(req.content, "html.parser")

threat_actors = [] # List of threat actors
result_dict = {} # Dictionary with threat_actor as key, # of posts as value

top_x = 5

# Get the names of all the threat actors
for tag in soup.find_all("h3"):
    threat_actor = tag.get('id')
    threat_actors.append(threat_actor)

# Get the number of posts of each threat actor
for threat_actor in threat_actors:
    # Upon inspection of html, the table that contains the posts of each threat actor is contained 2 divs away
    # from the h3 tag that holds the text "Posts"
    h3_tag = soup.find("h3", id=threat_actor) # Get the h3 tag that lists down threat actor name
    table = h3_tag.find_all_next("div")[1] # Get the second <div> element after the h3 tag
    tbody =  table.find("tbody") # Find the table body
    date = table.find("center")
    tr_tags = tbody.find_all("tr") # Get all the tr tags in table body
    num_tr_tags = len(tr_tags) # Compute the number of tr tags to get the number of posts
    
    for tr in tr_tags:
        date = tr.find("center").get_text()
        if '2023' not in date:
            num_tr_tags -= 1

    # print("Threat: ", threat_actor, "num posts: ", num_tr_tags)
    result_dict.update( {threat_actor: num_tr_tags} )

print(result_dict)


# Get the most top 3 active threat actors based on number of posts
sorted_dict = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
most_active_actors = [item[0] for item in sorted_dict[:top_x]]
print(most_active_actors)




