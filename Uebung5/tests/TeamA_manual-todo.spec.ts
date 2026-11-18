//implementiert von: JYBS RTRE

import { test, expect } from '@playwright/test';

test.describe('Manuell programmierte Tests', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://demo.playwright.dev/todomvc/');
  });

  test('Filterlogik überprüfen', async ({ page }) => {
    // 1. drei Todos anlegen und eins davon als erledigt markieren
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Einkaufen');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Lernen');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Putzen');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('listitem').filter({ hasText: 'Einkaufen' }).getByLabel('Toggle Todo').check();

    // 2. unten auf den Filter-Link Active klicken und mit toHaveCount(2) prüfen, dass nur die zwei offenen Einträge angezeigt werden.
    await page.getByRole('link', { name: 'Active' }).click();
    await expect(page.getByTestId('todo-item')).toHaveCount(2);

    // 3. auf Completed klicken und prüfen, dass genau ein Eintrag sichtbar ist (toHaveCount(1)).
    await page.getByRole('link', { name: 'Completed' }).click();
    await expect(page.getByTestId('todo-item')).toHaveCount(1);

   // 4. auf All klicken und verifizieren, dass wieder alle drei Einträge angezeigt werden (toHaveCount(3)).
    await page.getByRole('link', { name: 'All' }).click();
    await expect(page.getByTestId('todo-item')).toHaveCount(3);
  });

  test('Todo nachträglich bearbeiten und Bearbeitung mit Escape abbrechen', async ({ page }) => {
    // 1. ein Todo anlegen und einen Doppelklick auf den Titel ausführen (await locator.dblclick())
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByText('Kochen').dblclick();

    // 2. den Text im Bearbeitungsfeld ändern, mit Enter bestätigen und per Assertion prüfen, dass der neue Text übernommen wurde
    await page.getByRole('textbox', { name: 'Edit' }).click();
    await page.getByRole('textbox', { name: 'Edit' }).fill('Wohnung putzen');
    await page.getByRole('textbox', { name: 'Edit' }).press('Enter');
    await expect(page.getByTestId('todo-title')).toContainText('Wohnung putzen');
    //await expect(page.getByTestId('todo-item')).getByText('Wohnung putzen').toBeVisible();

    // 3. erneut auf denselben Eintrag Doppelklicken, einen anderen Text eintippen, aber mit der Taste Escape abbrechen. 
    // Prüfen, dass die Änderung verworfen wurde und der vorherige Text erhalten bleibt
    await page.getByText('Wohnung Putzen').dblclick();
    await page.getByRole('textbox', { name: 'Edit' }).fill('Haus Putzen');
    await page.getByRole('textbox', { name: 'Edit' }).press('Escape');
    await expect(page.getByTestId('todo-title')).toContainText('Wohnung putzen');
  });

  test('Erledigte Todos löschen und Seiten-Reload testen', async ({ page }) => {
    // 1. zwei Todos anlegen, eins als erledigt markieren und auf Clear completed klicken
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Waesche waschen');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Termin machen');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('listitem').filter({ hasText: 'Termin machen' }).getByLabel('Toggle Todo').check();
    await page.getByRole('button', { name: 'Clear completed' }).click();
    // 2. die Seite neu laden und prüfen, dass das gelöschte Todo auch nach dem Neuladen verschwunden bleibt und nur noch das offene Todo in der Liste steht 
    await expect(page.getByTestId('todo-item')).toHaveCount(1);
  });
});