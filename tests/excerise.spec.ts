import {expect, test, devices} from '@playwright/test';

test.use(devices['iPhone 11']);

test('should be titled', async ({page, context}) => {
    await context.route('**.jpg', route => route.abort());
    await page.goto('https://example.com/');

    await expect(page).toHaveTitle('Example');
});

test('homepage has Playwright in title and get started link linking to the intro page', async ({ page }) => {
    await page.goto('https://playwright.dev/');
  
    // Expect a title "to contain" a substring.
    await expect(page).toHaveTitle(/Playwright/);
  
    // create a locator
    const getStarted = page.locator('text=Get Started');
  
    // Expect an attribute "to be strictly equal" to the value.
    await expect(getStarted).toHaveAttribute('href', '/docs/intro');
  
    // Click the get started link.
    await getStarted.click();
  
    // Expects the URL to contain intro.
    await expect(page).toHaveURL(/.*intro/);
  });