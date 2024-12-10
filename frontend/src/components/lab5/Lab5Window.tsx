import { FC, useState, useEffect } from "react";
import {
    Button,
    NumberInput,
    Notification,
    Title,
    Divider,
    Flex,
    Box,
    Center,
} from "@mantine/core";
import axios from "axios";
import Tree from "react-d3-tree";

interface BTreeNode {
    keys: number[];
    children: BTreeNode[];
}

interface BTreeData {
    name: string;
    children: BTreeNode[];
}

const transformBTreeToD3Data = (node: any | undefined): any => {
    if (!node) {
        return null;
    }

    return {
        name: node.name || "Пустой узел",
        children: node.children.map(transformBTreeToD3Data),
    };
};

export const Lab5Window: FC = () => {
    const [key, setKey] = useState<number>();
    const [del_key, setDelKey] = useState<number>();
    const [search_key, setSearchKey] = useState<number>();
    const [treeData, setTreeData] = useState<BTreeData | null>(null);
    const [message, setMessage] = useState<string | null>(null);

    const getTreeStructure = async () => {
        try {
            const response = await axios.get(
                "http://37.128.205.70:3415/v1/lab_5/tree_structure"
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
                    "http://37.128.205.70:3415/v1/lab_5/insert",
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
                    "http://37.128.205.70:3415/v1/lab_5/del",
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
                const response = await axios.post(
                    "http://37.128.205.70:3415/v1/lab_5/search",
                    null,
                    {
                        params: { search_key },
                    }
                );
                setMessage(response.data.message);
                getTreeStructure();
            } catch (error) {
                setMessage("Ошибка при поиске ключа");
            }
        }
    };
    const clearTree = async () => {
        try {
            const response = await axios.post(
                "http://37.128.205.70:3415/v1/lab_5/clear"
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
                "http://37.128.205.70:3415/v1/lab_5/random_fill"
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
            <Title style={{ textAlign: "center" }}>🌳 B-дерево</Title>
            <Divider my="sm" />

            <Flex
                justify="center"
                direction={{ base: "column", md: "row" }}
                wrap="wrap"
                gap="sm"
                style={{
                    width: "100%",
                    paddingLeft: "3%",
                    paddingRight: "3%",
                }}
            >
                <NumberInput
                    value={key}
                    w="100%"
                    onChange={(value: string | number) =>
                        setKey(
                            typeof value === "number"
                                ? value
                                : parseFloat(value) || undefined
                        )
                    }
                />

                <Button
                    onClick={insertKey}
                    color="green"
                    style={{ width: "100%" }}
                >
                    Вставить ключ
                </Button>

                <NumberInput
                    value={search_key}
                    w="100%"
                    onChange={(value: string | number) =>
                        setSearchKey(
                            typeof value === "number"
                                ? value
                                : parseFloat(value) || undefined
                        )
                    }
                />

                <Button
                    color="orange"
                    onClick={searchKey}
                    style={{ width: "100%" }}
                >
                    Поиск ключа
                </Button>

                <NumberInput
                    value={del_key}
                    w="100%"
                    onChange={(value: string | number) =>
                        setDelKey(
                            typeof value === "number"
                                ? value
                                : parseFloat(value) || undefined
                        )
                    }
                />

                <Button
                    color="red"
                    onClick={deleteKey}
                    style={{ width: "100%" }}
                >
                    Удалить ключ
                </Button>

                <Divider my={"sm"} />
                <Button onClick={clearTree} style={{ width: "100%" }}>
                    Очистить дерево
                </Button>
                <Button onClick={randomFill} style={{ width: "100%" }}>
                    Заполнить случайными ключами
                </Button>
            </Flex>

            {message && (
                <Notification
                    color="teal"
                    onClose={() => setMessage(null)}
                    style={{
                        position: "fixed",
                        top: 60, // Размещение уведомления сверху
                        left: "50%", // Центровка по горизонтали
                        transform: "translateX(-50%)", // Сдвиг на половину ширины, чтобы точно центрировать
                        zIndex: 1000,
                    }}
                >
                    {message}
                </Notification>
            )}

            <Divider my="sm" />
            <div
                style={{
                    width: "100%",
                    height: "50vh",
                    overflow: "auto",
                    backgroundColor: "gray",
                    scrollBehavior: "smooth",
                }}
            >
                {treeData ? (
                    <Box
                        style={{
                            height: "100%",
                            display: "flex",
                            justifyContent: "center",
                            alignItems: "center",
                        }}
                    >
                        <Tree
                            data={transformBTreeToD3Data(treeData)}
                            orientation="vertical"
                            pathFunc="straight"
                            translate={{ x: 500, y: 50 }}
                        />
                    </Box>
                ) : (
                    <Box
                        style={{
                            height: "100%",
                            display: "flex",
                            justifyContent: "center",
                            alignItems: "center",
                            textAlign: "center",
                        }}
                    >
                        <Center>
                            <text color="dimmed">Дерево пусто</text>
                        </Center>
                    </Box>
                )}
            </div>
        </div>
    );
};
