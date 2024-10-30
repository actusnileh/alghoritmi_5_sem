import { FC, useState, useEffect } from "react";
import {
    Button,
    Group,
    NumberInput,
    Notification,
    Title,
    Divider,
} from "@mantine/core";
import axios from "axios";
import Tree from "react-d3-tree";

interface AVLTreeNode {
    keys: number[];
    children: AVLTreeNode[];
}

interface AVLTreeData {
    name: string;
    children: AVLTreeNode[];
}

const transformAVLTreeToD3Data = (node: any | undefined): any => {
    if (!node) {
        return null;
    }

    return {
        name: node.name || "Пустой узел",
        children: node.children.map(transformAVLTreeToD3Data),
    };
};

export const Lab6Window: FC = () => {
    const [key, setKey] = useState<number>();
    const [del_key, setDelKey] = useState<number>();
    const [search_key, setSearchKey] = useState<number>();
    const [treeData, setTreeData] = useState<AVLTreeData | null>(null);
    const [message, setMessage] = useState<string | null>(null);
    const [treeHeight, setTreeHeight] = useState<number | null>(null);
    const getTreeStructure = async () => {
        try {
            const response = await axios.get(
                "http://0.0.0.0:8000/v1/lab_6/tree_structure"
            );
            const bTreeData = response.data.tree;
            setTreeData(bTreeData);
        } catch (error) {
            setMessage("Ошибка при получении структуры дерева");
        }
    };

    const insertKey = async () => {
        if (key !== null) {
            try {
                const response = await axios.post(
                    "http://0.0.0.0:8000/v1/lab_6/insert",
                    null,
                    {
                        params: { key },
                    }
                );
                setMessage(response.data.message);
                getTreeStructure();
            } catch (error) {
                setMessage("Ошибка при вставке ключа");
            }
        }
    };

    const deleteKey = async () => {
        if (del_key !== null) {
            try {
                const response = await axios.post(
                    "http://0.0.0.0:8000/v1/lab_6/del",
                    null,
                    {
                        params: { del_key },
                    }
                );
                setMessage(response.data.message);
                getTreeStructure();
            } catch (error) {
                setMessage("Ошибка при удалении ключа");
            }
        }
    };

    const searchKey = async () => {
        if (search_key !== null) {
            try {
                const response = await axios.get(
                    "http://0.0.0.0:8000/v1/lab_6/search",
                    {
                        params: { key: search_key },
                    }
                );
                setMessage(response.data.message);
                getTreeStructure();
            } catch (error) {
                setMessage("Ошибка при поиске ключа");
            }
        }
    };
    const getHeight = async () => {
        try {
            const response = await axios.get(
                "http://0.0.0.0:8000/v1/lab_6/height"
            );
            setTreeHeight(response.data.height);
            setMessage(`Высота дерева: ${response.data.height}`);
        } catch (error) {
            setMessage("Ошибка при получении высоты дерева");
        }
    };
    const clearTree = async () => {
        try {
            const response = await axios.post(
                "http://0.0.0.0:8000/v1/lab_6/clear"
            );
            setMessage(response.data.message);
            getTreeStructure();
        } catch (error) {
            setMessage("Ошибка при очистке дерева");
        }
    };

    const randomFill = async () => {
        try {
            const response = await axios.post(
                "http://0.0.0.0:8000/v1/lab_6/random_fill"
            );
            setMessage(response.data.message);
            getTreeStructure();
        } catch (error) {
            setMessage("Ошибка при заполнении случайными ключами");
        }
    };

    useEffect(() => {
        getTreeStructure();
    }, []);

    return (
        <div>
            <Title style={{ textAlign: "center" }}>
                AVL-дерево Визуализация
            </Title>{" "}
            <Divider my="sm"></Divider>
            <Group justify="center">
                <NumberInput
                    value={key}
                    w={"100px"}
                    onChange={(value) => setKey(value)}
                />
                <Button onClick={insertKey} color="green">
                    Вставить ключ
                </Button>
                <NumberInput
                    value={search_key}
                    w={"100px"}
                    onChange={(value) => setSearchKey(value)}
                />
                <Button color="orange" onClick={searchKey}>
                    Поиск ключа
                </Button>
                <NumberInput
                    value={del_key}
                    w={"100px"}
                    onChange={(value) => setDelKey(value)}
                />
                <Button color="red" onClick={deleteKey}>
                    Удалить ключ
                </Button>
                <Divider me={"xl"} />
                <Button onClick={clearTree}>Очистить дерево</Button>
                <Button onClick={randomFill}>
                    Заполнить случайными ключами
                </Button>
                <Button onClick={getHeight}>Высота дерева</Button>{" "}
            </Group>
            {message && (
                <Notification
                    color="teal"
                    onClose={() => setMessage(null)}
                    style={{
                        position: "fixed",
                        bottom: 20,
                        left: 20,
                        zIndex: 1000,
                    }}
                >
                    {message}
                </Notification>
            )}
            <Divider my="sm"></Divider>
            <div
                style={{
                    height: "100vh",
                    backgroundColor: "gray",
                }}
            >
                {treeData ? (
                    <Tree
                        data={transformAVLTreeToD3Data(treeData)}
                        orientation="vertical"
                        pathFunc="straight"
                        translate={{ x: 500, y: 50 }}
                    />
                ) : (
                    <div />
                )}
            </div>
        </div>
    );
};
