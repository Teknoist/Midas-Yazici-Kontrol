const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  
  await page.goto('http://localhost:5174');
  await page.evaluate(() => {
    window.api = window.api || {};
    // PWA store overrides
    localStorage.setItem('nova_settings', JSON.stringify({ theme: 'light', accent: '#36d399' }));
  });
  
  await page.reload();
  await page.waitForTimeout(2000); 
  
  // Take Light Mode screenshot
  await page.screenshot({ path: 'docs/screenshots/overview-light.png' });
  
  await browser.close();
})();
