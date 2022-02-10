const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch({
    bindAddress: "0.0.0.0",
    args: [
      "--headless",
      "--disable-gpu",
      "--disable-dev-shm-usage",
      "--remote-debugging-port=9222",
      "--remote-debugging-address=0.0.0.0"
    ]
  });
 const page = await browser.newPage();
  // await page.setViewport({ width: 412, height: 732 });
  await page.emulateMediaType('screen');
	{% for file in files %}
  await page.goto("file://{{ file.get('in_path') }}", { waitUntil: "networkidle2" });
  await page.pdf({ path: "{{ file.get('out_path') }}", format: "A4", printBackground: true });
	{% endfor %}
  await browser.close();
})();
