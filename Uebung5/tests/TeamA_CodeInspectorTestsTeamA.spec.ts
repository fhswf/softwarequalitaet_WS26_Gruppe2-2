//implementiert von: JYBS RTRE
import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://demo.playwright.dev/todomvc/#/');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Test');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByTestId('todo-title').click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Test');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('ArrowDown');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('NumLock');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Test2');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('link', { name: 'Active' }).click();
  await expect(page.getByRole('link', { name: 'Completed' })).toBeVisible();
  await expect(page.locator('body')).toContainText('Test');
  await expect(page.getByRole('textbox', { name: 'What needs to be done?' })).toBeEmpty();
  await page.getByText('Test2').click();
  await expect(page.getByRole('textbox', { name: 'What needs to be done?' })).toBeEmpty();
});