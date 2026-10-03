const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  
  await page.goto('http://localhost:5173');
  await page.waitForTimeout(2000); // Wait for animations
  await page.screenshot({ path: 'docs/screenshots/overview.png' });
  
  // Click Printers
  await page.click('text=Filo'); // "Filo" or "Printers" depending on locale. Oh wait, we're in TR? The preview might be TR because OS is TR.
  // Actually let's just click the second nav item.
  await page.click('nav > button:nth-child(2)');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'docs/screenshots/printers.png' });
  
  // Click Files
  await page.click('nav > button:nth-child(3)');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'docs/screenshots/file-center.png' });

  // Android version overview
  const mobilePage = await browser.newPage({ viewport: { width: 412, height: 915 } });
  await mobilePage.goto('http://localhost:5173');
  await mobilePage.waitForTimeout(2000);
  await mobilePage.screenshot({ path: 'docs/screenshots/android-overview.png' });

  await browser.close();
})();
