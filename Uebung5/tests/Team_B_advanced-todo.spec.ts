#NOVE
#TNSS

import { expect, Page, test } from '@playwright/test';

const TODO_URL = 'https://demo.playwright.dev/todomvc/';

async function addTodo(page: Page, text: string) {
    const newTodoInput = page.getByPlaceholder('What needs to be done?');
    await newTodoInput.fill(text);
    await newTodoInput.press('Enter');
}

test.beforeEach(async ({ page }) => {
    await page.goto(TODO_URL);
});

test('Leere und aus Leerzeichen bestehende Eingaben werden abgewiesen', async ({ page }) => {
    const newTodoInput = page.getByPlaceholder('What needs to be done?');
    await newTodoInput.press('Enter');
    await newTodoInput.fill(' ');
    await newTodoInput.press('Enter');

    await expect(page.getByTestId('todo-item')).toHaveCount(0);
    await expect(page.getByTestId('footer')).toBeHidden();
});

test('Toggle All aktualisiert Todos und Zähler synchron', async ({ page }) => {
    await addTodo(page, 'Todo 1');
    await addTodo(page, 'Todo 2');
    await addTodo(page, 'Todo 3');

    const items = page.getByTestId('todo-item');
    const toggleAll = page.getByLabel('Mark all as complete');
    await toggleAll.click();

    await expect(page.getByTestId('todo-count')).toContainText('0 items left');
    for (const item of await items.all()) {
        await expect(item).toHaveClass(/completed/);
    }

    await toggleAll.click();
    await expect(page.getByTestId('todo-count')).toContainText('3 items left');
});

test('Ein Todo lässt sich über den Hover-Button löschen', async ({ page }) => {
    await addTodo(page, 'Zu löschendes Todo');

    const todoItem = page.getByTestId('todo-item');
    await todoItem.hover();
    await todoItem.getByRole('button', { name: 'Delete' }).click();

    await expect(page.getByTestId('todo-item')).toHaveCount(0);
});

test('Todos werden im localStorage gespeichert', async ({ page }) => {
    await addTodo(page, 'Erledigtes Todo');
    await addTodo(page, 'Offenes Todo');
    await page.getByTestId('todo-item').nth(0).getByRole('checkbox').check();

    const storedData = await page.evaluate(() => localStorage.getItem('react-todos'));
    const todos: { completed: boolean }[] = JSON.parse(storedData ?? '[]');

    expect(todos).toHaveLength(2);
    expect(todos[0].completed).toBe(true);
});
