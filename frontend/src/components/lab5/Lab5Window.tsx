import {
    Container,
    Title,
    TextInput,
    Button,
    Notification,
} from "@mantine/core";
import { FC, useEffect, useState } from "react";
import axios from "axios";
import Tree from "react-d3-tree";

export const Lab5Window: FC = () => {
    const [key, setKey] = useState<number>(0);
    const [searchKey, setSearchKey] = useState<number>(0);
    const [notification, setNotification] = useState<{
        message: string;
        color: string;
    } | null>(null);
    const [treeData, setTreeData] = useState<any>(null);

    // Функция для получения структуры дерева
    const fetchTree = async () => {
        try {
            const response = await axios.get(
                "http://0.0.0.0:8000/v1/lab_5/tree_structure"
            );
            setTreeData(response.data);
        } catch (error) {
            setNotification({
                message: "Ошибка получения дерева",
                color: "red",
            });
        }
    };

    // Функция для получения структуры дерева
    const clearTree = async () => {
        try {
            await axios.post("http://0.0.0.0:8000/v1/lab_5/clear");
        } catch (error) {
            setNotification({
                message: "Ошибка очистки дерева",
                color: "red",
            });
        }
    };
    // Функция для вставки ключа
    const handleInsert = async () => {
        try {
            await axios.post("http://0.0.0.0:8000/v1/lab_5/insert", null, {
                params: { key },
            });
            setNotification({ message: `Вставлено: ${key}`, color: "green" });
            fetchTree();
        } catch (error) {
            setNotification({ message: "Ошибка вставки", color: "red" });
        }
    };

    // Функция для поиска ключа
    const handleSearch = async () => {
        try {
            const response = await axios.get(
                `http://0.0.0.0:8000/v1/lab_5/search`,
                { params: { key: searchKey } }
            );
            setNotification({ message: response.data.message, color: "blue" });
        } catch (error) {
            setNotification({ message: "Ключ не найден", color: "red" });
        }
    };

    // Функция для заполнения дерева случайными ключами
    const handleRandomFill = async () => {
        try {
            await axios.post("http://0.0.0.0:8000/v1/lab_5/random_fill");
            setNotification({
                message: "Дерево заполнено случайно",
                color: "green",
            });
            fetchTree();
        } catch (error) {
            setNotification({ message: "Ошибка заполнения", color: "red" });
        }
    };

    // Получаем дерево при монтировании компонента
    useEffect(() => {
        fetchTree();
    }, []);

    return (
        <Container
            my="xl"
            style={{ alignItems: "center", textAlign: "center" }}
        >
            <Title order={2} mb="xl">
                Лаб. работа №5
            </Title>
            <Button onClick={handleRandomFill} mb="md" mr="md">
                Заполнить случайно
            </Button>
            <Button onClick={clearTree} color={"red"} mb="md">
                Очистить
            </Button>
            <TextInput
                placeholder="Ключ для вставки"
                label="Ключ"
                value={key}
                onChange={(e) => setKey(Number(e.currentTarget.value))}
                mb="md"
            />
            <Button mb="xl" onClick={handleInsert}>
                Вставить
            </Button>

            <TextInput
                placeholder="Ключ для поиска"
                label="Ключ для поиска"
                value={searchKey}
                onChange={(e) => setSearchKey(Number(e.currentTarget.value))}
                mb="md"
            />
            <Button onClick={handleSearch} mb="md">
                Поиск
            </Button>

            {notification && (
                <Notification
                    color={notification.color}
                    onClose={() => setNotification(null)}
                    mt="md"
                >
                    {notification.message}
                </Notification>
            )}

            {treeData && (
                <div
                    style={{
                        height: "500px",
                        marginTop: "20px",
                        backgroundColor: "white",
                        color: "black",
                        border: "1px solid #ccc",
                        borderRadius: "4px",
                        overflow: "auto", // Добавьте прокрутку при необходимости
                    }}
                >
                    <Tree data={treeData} orientation="vertical" />
                </div>
            )}
        </Container>
    );
};
