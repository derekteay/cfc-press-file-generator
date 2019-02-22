from airtable import Airtable
import sys
from datetime import datetime
from bs4 import BeautifulSoup

# AirTable API setup
airtable = Airtable('base-key', 'table name', api_key='your-api-key')

# Get only records that are in the correct Status
records = airtable.get_all(view='Sorted')

# Create defaultdict structure
records_list = []

# Process each record from AirTable
for record in records:

    #print(record)

    # For ease of code writing
    record = record['fields']

    # Sanitize bad data in AirTable - Formatting the information
    try:
        title = record['Title']
    except KeyError:
        title = 'BLANK'

    try:
        url = record['URL']
    except KeyError:
        url = 'BLANK'

    try:
        date = record['Date']

        # Convert date format from AirTable, even though the data is in there correctly, the API pulls down a different formatted date
        date = datetime.strptime(date, '%Y-%m-%d')

        # Remove leading 0 from dates
        date = datetime.strftime(date, '%B %d, %Y').replace(" 0", " ")
    except KeyError:
        date = 'BLANK'

    try:
        company = record['Company']
    except KeyError:
        company = 'BLANK'

    try:
        desc = record['Description']
    except KeyError:
        desc = 'BLANK'

    # Create event list dictionary
    item = {"title": title,
            "url": url,
            "date": date,
            "company": company,
            "desc": desc}

    records_list.append(item)

# Write to press.html file
stdout = sys.stdout
sys.stdout = open('press_unformatted.html', 'w')

# Static content of HTML file
print('''<script type="text/javascript">
window.onload = function () {
var e1 = document.getElementById("ginni-news");
var w1 = parseFloat(e1.offsetWidth);
var h1 = parseFloat(e1.offsetHeight);
var e2 = document.getElementById("bob-news");
var w2 = e2.offsetWidth;
var h2 = e2.offsetHeight;

if (w1 / h1 >= 1.5) {
  e1.style = "background:url(/wp-content/uploads/2018/06/CFC-presspage-image1-horizontal.jpg) center top no-repeat; background-size:cover;";
} else if (w1 / h1 >= 0.9 && w1 / h1 <= 1.1) {
  e1.style = "background:url(/wp-content/uploads/2018/06/CFC-presspage-image1-square.jpg) center top no-repeat; background-size:cover;";
} else {
  e1.style = "background:url(/wp-content/uploads/2018/06/CFC-presspage-image1.jpg) center top no-repeat;background-size:cover;";
}
if (w2 / h2 >= 1.2) {
  e2.style = "background:url(/wp-content/uploads/2018/06/CFC-press-image2-horizontal.jpg) left top no-repeat; background-size:cover;";
} else {
  e2.style = "background:url(/wp-content/uploads/2018/06/CFC-press-image2.jpg) left top no-repeat;background-size:cover;";
}
}
</script>

<div class="hero1">
<div class="car">
<div class="leadspace-body">
  <h3>Call
    <span>For</span> Code</h3>
  <h1>Press</h1>
</div>
</div>
</div>

<div class="bx--grid--top">
<div class="bx--row">
<div id="ginni-news" class="bx--col-xs-12 bx--col-md-6 press-card-left" style="background:url(/wp-content/uploads/2018/06/CFC-presspage-image1.jpg) left top no-repeat; background-size:contain; background-color:black">
  <a href="https://www.cnbc.com/video/2018/05/24/ibm-ceo-our-blockchain-runs-on-our-public-cloud.html"></a>
</div>

<div class="bx--col-xs-12 bx--col-md-6 press-card-right" style="background-color:black">
  <h4 class="press-card-content__title">
    <span style="color: #469AD8;">CALL FOR CODE</span> IN THE NEWS</h4>
  <p>In addition, the company announced a new 'Call for Code' initiative that would use cloud, data, AI, and
    blockchain
    technologies to create systems that allow for better responses to natural disasters around the globe. Rometty
    said IBM would spend $30 million over five years to rally developers around this initiative.
    <br />
    <span style="color:#469AD8;">–
      <a href="https://venturebeat.com/2018/05/24/ibm-ceo-ginni-rometty-calls-on-developers-to-embrace-responsible-ai-principles/">VentureBeat</a>
    </span>
  </p>
  <p>IBM is an acknowledged leader in the use of blockchain for financial and enterprise reasons, and its Watson AI
    services are popular in certain areas like health care. So making these technologies available, along with
    the $30 million pledge, encourages coders to gain experience with IBM's tech, while also serving a cause.
    <br />
    <span style="color:#469AD8;">–
      <a href="http://www.businessinsider.com/ibm-call-for-code-natural-disaster-relief-2018-5">Business Insider</a>
    </span>
  </p>
</div>
</div>

<div class="bx--row">
<div class="bx--col-xs-12 bx--col-md-6 press-card-left" style="background-color:#2DAFFC">
  <p>“We cannot attempt to prevent earthquakes from happening or prevent hurricanes from happening around the
    globe,”
    said Bob Lord, IBM’s chief digital officer, who dropped by Fortune’s offices to discuss the new program.
    “But what we can do is unleash our tools and other tools so developers can help geographic regions get prepared
    for those natural disasters that happen.”
    <br />
    <span>–
      <a href="https://for.tn/2H3zQpK" style="color:#fff">Fortune</a>
    </span>
  </p>
  <p>From today until September 28, Argentine and world developers can participate in Call for Code, an initiative to
    create applications that mitigate risk in environmental disasters and help citizens recover as quickly as
    possible.
    <br />
    <span>–
      <a href="https://www.lanacion.com.ar/2137624-call-for-code-escribir-aplicaciones-para-ayudar-al-medio-ambiente"
        style="color:#fff">La Nacion (Argentina)</a>
    </span>
  </p>
</div>

<div id="bob-news" class="bx--col-xs-12 bx--col-md-6 press-card-right" style="background:url(/wp-content/uploads/2018/06/CFC-press-image2.jpg) right top no-repeat; background-size:contain; background-color:#2DAFFC">
  <a href="https://app.criticalmention.com/app/#/report/d1cb33c6-6f0d-46ef-964e-ada1a1144557"></a>
</div>
</div>
</div>

<section>
<div class="car">
<div class="leadspace-body">

  <div class="bx--grid affiliates" data-widget="setsameheight" data-items=".cfc--card">''')

counter = 0

for item in records_list:
    #print(item)

    # Every 3 items, create a new row
    if(counter%4 == 0):
        print('<div class="bx--row">')
        counter += 1

    print('''<div class="bx--col-xs-12 bx--col-md-4">
        <!-- start card -->
        <div class="cfc--card">
          <div class="cfc--card__body">
            <a href="''' + item['url'] + '''"
              class="">
              <h3 class="cfc--card__title">
                <a href="''' + item['url'] + '''">''' + item['title'] + '''</a>
              </h3>
              <p class="cfc--card__excerpt">''' + item['company'] + '''</p>
            </a>
            <p class="cfc--card__date">''' + item['date'] + '''</p>
            <p class="cfc--card__excerpt">''' + item['desc'] + '''</p>
          </div>
        </div>
        <!-- end card -->
        </div>''')

    counter += 1

    # Every 3 items, close the row div
    if(counter%4 == 0):
        print("""</div>
            <p> </p>""")


sys.stdout = stdout

# Open the unformatted file for formatting
press_file = open('press_unformatted.html', 'r')
content = press_file.read()
press_file.close()

# Prettify the html file
soup = BeautifulSoup(content, 'html.parser')
formatted_text = soup.prettify()

# Write the prettify'd file
file = open("press.html", "w")
file.write(formatted_text)
file.close()

print("Done!")