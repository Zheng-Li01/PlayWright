

// import { test, expect } from '@playwright/test';
// import AxeBuilder from '@axe-core/playwright';
// import { chromium, FullConfig } from '@playwright/test';
// import { request } from '@playwright/test';

// async function globalSetup() {
//     const requestContext = await request.newContext();
//     await requestContext.post('https://github.com/login',{
//     form: {
//         'user':'user',
//         'password':'password'
//     }        
// });

// await requestContext.storageState({ path: 'storageState.json' });
// await requestContext.dispose();
// }

// export default globalSetup;
// async function globalSetup(config: FullConfig) {
//     const browser = await chromium.launch();
//     const page = await browser.newPage();
//     await page.goto('https://github.com/login');
//     await page.locator('input[name="login"]').fill('user');
//     await page.locator('inout[name="passwird"]').fill('password');
//     await page.context().storageState({ path: 'storageState.json'});
//     await browser.close();
// } 

// export default globalSetup;

// test.beforeEach(async ({ page }) =>{
//     await page.goto('https://github.com/login');
//     await page.locator('text=login').count();
//     await page.locator('input[name="login"]').fill('username');
//     await page.locator('input[name="password"]').fill('password');
//     await page.locator('text=Submit').click();
// });

// // playwright.config.ts
// import type { PlaywrightTestConfig } from '@playwright/test';

// const config: PlaywrightTestConfig = {
//   globalSetup: require.resolve('./global-setup'),
//   use: {
//     // Tell all tests to load signed-in state from 'storageState.json'.
//     storageState: 'storageState.json'
//   }
// };
// export default config;
// test('should not have any accessibility violations outside of elements with known issues', async ({ page }) => {
//     await page.goto('https://your-site.com/page-with-known-issues');
  
//     const accessibilityScanResults = await new AxeBuilder({ page })
//       .exclude('#element-with-known-issue')
//       .analyze();
  
//     expect(accessibilityScanResults.violations).toEqual([]);
//   });
// test('should not have any automatically detectable WCAG A or AA violations', async ({ page }) => {
//     await page.goto('https://your-site.com/');
  
//     const accessibilityScanResults = await new AxeBuilder({ page })
//       .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
//       .analyze();
  
//     expect(accessibilityScanResults.violations).toEqual([]);
//   });
// test('navigation menu flyout should not have automatically detectable accessibility violations', async ({ page }) => {
//     await page.goto('https://your-site.com/');
  
//     await page.locator('button[aria-label="Navigation Menu"]').click();
  
//     // It is important to waitFor() the page to be in the desired
//     // state *before* running analyze(). Otherwise, axe might not
//     // find all the elements your test expects it to scan.
//     await page.locator('#navigation-menu-flyout').waitFor();
  
//     const accessibilityScanResults = await new AxeBuilder({ page })
//       .include('#navigation-menu-flyout')
//       .analyze();
  
//     expect(accessibilityScanResults.violations).toEqual([]);
//   });

// test.describe('homepage', () => {
//     test('should not have automatically detectable accessibility issues', async ({ page }) => {
//         await page.goto('https://your-site.com/');

//         const accessibilityScanResults = await new AxeBuilder({ page }).analyze();

//         expect(accessibilityScanResults.violations).toEqual([]);
//     });
// });
// import {expect, test, devices} from '@playwright/test';

// test.use(devices['iPhone 11']);

// test('should be titled', async ({page, context}) => {
//     await context.route('**.jpg', route => route.abort());
//     await page.goto('https://example.com/');

//     await expect(page).toHaveTitle('Example');
// });

// test('homepage has Playwright in title and get started link linking to the intro page', async ({ page }) => {
//     await page.goto('https://playwright.dev/');
  
//     // Expect a title "to contain" a substring.
//     await expect(page).toHaveTitle(/Playwright/);
  
//     // create a locator
//     const getStarted = page.locator('text=Get Started');
  
//     // Expect an attribute "to be strictly equal" to the value.
//     await expect(getStarted).toHaveAttribute('href', '/docs/intro');
  
//     // Click the get started link.
//     await getStarted.click();
  
//     // Expects the URL to contain intro.
//     await expect(page).toHaveURL(/.*intro/);
//   });