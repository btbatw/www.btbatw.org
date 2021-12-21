import csv
import yaml


lll = yaml.load(open('leadership.yml'))

for k in lll['leaderships']:

    ddd = lll['leaderships'][k]
    with open(f"{k}.csv", 'w', newline='') as csvfile:
        fieldnames = [
            'Name in English',
            'Name in Chinese',
            'Email',
            'Position title on the website',
            'Position in the BTBA Committee',
            'Team',
            'Job Title & Affiliation',
            'LinkedIn',
            'Headshot Name'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for rrr in ddd:
            position = rrr['position']
            if rrr['current'] is not None:
                position += f" (Current: {rrr['current']})"
            writer.writerow({
                'Name in English': rrr['name'],
                'Name in Chinese': rrr['ch-name'],
                'Position title on the website': 'Co-president',
                'Job Title & Affiliation': position,
                'Headshot Name': rrr['image-url'].split('/')[-1]
            })
