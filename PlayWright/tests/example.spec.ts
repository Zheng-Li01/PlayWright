


// import { test, expect } from '@playwright/test'

// test('basic test', async ({page}) => {
//     await page.goto('https://playwright.dev/')
//     const title = page.locator('.navbar__inner .navbar__title')
//     await expect(title).toHaveText('Playwright')
// });

// import { test, expect } from '@playwright/test';

// test('homepage has Playwright in title and get started link linking to the intro page', async ({ page }) => {
//   await page.goto('https://playwright.dev/');

//   // Expect a title "to contain" a substring.
//   await expect(page).toHaveTitle(/Playwright/);

//   // create a locator
//   const getStarted = page.locator('text=Get Started');

//   // Expect an attribute "to be strictly equal" to the value.
//   await expect(getStarted).toHaveAttribute('href', '/docs/intro');

//   // Click the get started link.
//   await getStarted.click();

//   // Expects the URL to contain intro.
//   await expect(page).toHaveURL(/.*intro/);
// });


// test.describe("navigation", () => {
//   test.beforeEach(async ({ page}) => {
//     // Go to the starting url before each tes.
//     await page.goto("https://playwright.dev/");
//   });

//   test("main navigation", async ({page}) => {
//     // Assertions use the expect API.
//     await expect(page).toHaveURL("https://playwright.dev/")
//   });
// });

// import { test, expect } from '@playwright/test';

// test('test', async ({ page }) => {

//   // Go to http://playwright.dev/
//   await page.goto('http://playwright.dev/');

//   // Click a:has-text("Docs")
//   await page.locator('a:has-text("Docs")').click();
//   await expect(page).toHaveURL('http://playwright.dev/docs/intro');

//   // Click article a:has-text("What's Installed")
//   await page.locator('article a:has-text("What\'s Installed")').click();
//   await expect(page).toHaveURL('http://playwright.dev/docs/intro#whats-installed');

//   // Click text=The playwright.config is where you can add configuration for Playwright includin
//   await page.locator('text=The playwright.config is where you can add configuration for Playwright includin').click();

//   // Click text=The playwright.config is where you can add configuration for Playwright includin
//   await page.locator('text=The playwright.config is where you can add configuration for Playwright includin').click();

//   // Click text=The playwright.config is where you can add configuration for Playwright includin
//   await page.locator('text=The playwright.config is where you can add configuration for Playwright includin').click();

// });
// import { test, expect } from '@playwright/test';
// test('global context request has isolated cookie storage', async ({ page, context, browser, playwright }) => {
//   // Create a new instance of APIRequestContext with isolated cookie storage.
//   const request = await playwright.request.newContext();
//   await context.route('https://www.github.com/', async (route) => {
//     const response = await request.fetch(route.request());
//     const responseHeaders = response.headers();

//     const responseCookies = new Map(responseHeaders['set-cookie'].split('\n').map(c => c.split(';', 2)[0].split('=')));
//     // The response will have 3 cookies in 'Set-Cookie' header.
//     expect(responseCookies.size).toBe(3);
//     const contextCookies = await context.cookies();
//     // The browser context will not have any cookies from the isolated API request.
//     expect(contextCookies.length).toBe(0);

//     // Manually export cookie storage.
//     const storageState = await request.storageState();
//     // Create a new context and initialize it with the cookies from the global request.
//     const browserContext2 = await browser.newContext({ storageState });
//     const contextCookies2 = await browserContext2.cookies();
//     // The new browser context will already contain all the cookies from the API response.
//     expect(new Map(contextCookies2.map(({name, value}) => [name, value]))).toEqual(responseCookies);

//     route.fulfill({
//       response,
//       headers: {...responseHeaders, foo: 'bar'},
//     });
//   });
//   await page.goto('https://www.github.com/');
//   await request.dispose();
// });