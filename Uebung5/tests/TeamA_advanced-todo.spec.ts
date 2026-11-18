import { test, expect } from '@playwright/test';

test.describe('Fortgeschrittene Testfälle', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://demo.playwright.dev/todomvc/');
  });

  test('Abweisung leerer Eingaben', async ({ page }) => {
    // 1. im leeren Eingabefeld Enter drücken und versuchen, ein neues Todo aus reinen Leerzeichen einzugeben
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('             ');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    // 2. prüfen, dass keine Einträge in der Liste erzeugt werden und die Fußzeile ausgeblendet bleibt
    await expect(page.getByTestId('todo-item')).toHaveCount(0);
    await expect(page.getByRole('button')).toBeHidden();
  });

  test('Alle-markieren Funktion und Zähler-Synchronisation', async ({ page }) => {
    // 1. drei Todos anlegen und auf das Pfeil-Symbol klicken, um alle Einträge gleichzeitig abzuhaken
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Todo 1');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Todo 2');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Todo 3');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByText('Mark all as complete').click();
    // 2. prüfen, dass "0 items left" angezeigt wird und alle Listenelemente "completed" besitzen
    await expect(page.locator('body')).toContainText('0 items left');
    for (const todo of await page.getByTestId('todo-item').all()) {
        await expect(todo).toHaveClass(/completed/);
    }
    // 3. erneut auf "Mark all as complete" klicken und prüfen, dass wieder "3 items left" angezeigt wird 
    await page.getByText('Mark all as complete').click();
    await expect(page.locator('body')).toContainText('3 items left');
  });

  test('Einzelnes Todo über das Hover-Symbol löschen', async ({ page }) => {
    // 1. Das rote Lösch-Kreuz rechts neben einem Eintrag erscheint erst, wenn sich der Mauszeiger über dem Todo befindet
    // Todo anlegen, Maus darüberbewegen, auf erscheinenden Button klicken und verifizieren, dass die Liste danach leer ist
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Todo 4');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByText('Todo 4').hover();
    await page.getByRole('button', { name: 'Delete' }).click();
    await expect(page.getByTestId('todo-item')).toHaveCount(0);
  });

  test('Datenpersistenz im localStorage überprüfen', async ({ page }) => {
    // 1. zwei Todos hinzufügen und das erste als erledigt markieren
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Todo 5');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
    await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Todo 6');
    await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    await page.getByRole('listitem').filter({ hasText: 'Todo 5' }).getByLabel('Toggle Todo').check();
    // 2. Browser-Speicher im Test auslesen
    const storedData = await page.evaluate(() => localStorage.getItem('react-todos'));
    const todos = JSON.parse(storedData ?? '[]');
    // 3. prüfen, dass die Daten korrekt im Browser gespeichert wurden
    expect(todos).toHaveLength(2);
    expect(todos[0].completed).toBe(true)
  });


});