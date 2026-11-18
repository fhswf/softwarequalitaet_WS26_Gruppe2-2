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

test('Filter All, Active und Completed zeigen die passenden Todos', async ({ page }) => {
    await addTodo(page, 'Todo 1');
    await addTodo(page, 'Todo 2');
    await addTodo(page, 'Todo 3');
    await page.getByTestId('todo-item').nth(0).getByRole('checkbox').check();

    await page.getByRole('link', { name: 'Active' }).click();
    await expect(page.getByTestId('todo-item')).toHaveCount(2);

    await page.getByRole('link', { name: 'Completed' }).click();
    await expect(page.getByTestId('todo-item')).toHaveCount(1);

    await page.getByRole('link', { name: 'All' }).click();
    await expect(page.getByTestId('todo-item')).toHaveCount(3);
});

test('Todo bearbeiten und eine weitere Bearbeitung mit Escape abbrechen', async ({ page }) => {
    await addTodo(page, 'Ursprüngliches Todo');

    const todoItem = page.getByTestId('todo-item');
    await todoItem.getByText('Ursprüngliches Todo').dblclick();

    const editInput = todoItem.locator('.edit');
    await editInput.fill('Bearbeitetes Todo');
    await editInput.press('Enter');
    await expect(todoItem.getByText('Bearbeitetes Todo')).toBeVisible();

    await todoItem.getByText('Bearbeitetes Todo').dblclick();
    await editInput.fill('Verworfene Änderung');
    await editInput.press('Escape');

    await expect(todoItem.getByText('Bearbeitetes Todo')).toBeVisible();
    await expect(page.getByText('Verworfene Änderung')).toHaveCount(0);
});

test('Clear completed bleibt nach einem Seiten-Reload erhalten', async ({ page }) => {
    await addTodo(page, 'Erledigtes Todo');
    await addTodo(page, 'Offenes Todo');
    await page.getByTestId('todo-item').nth(0).getByRole('checkbox').check();
    await page.getByRole('button', { name: 'Clear completed' }).click();

    await page.reload();

    await expect(page.getByTestId('todo-item')).toHaveCount(1);
    await expect(page.getByText('Erledigtes Todo')).toHaveCount(0);
    await expect(page.getByText('Offenes Todo')).toBeVisible();
});
